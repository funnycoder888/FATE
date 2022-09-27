#
#  Copyright 2019 The Eggroll Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from collections import Iterable
from typing import Optional

from ..._standalone import Session
from ...abc import AddressABC, CSessionABC
from ...common.log import getLogger
from ...unify import generate_computing_uuid, uuid
from ._table import Table

LOGGER = getLogger()


class CSession(CSessionABC):
    def __init__(
        self, session_id: Optional[str] = None, options: Optional[dict] = None
    ):
        if session_id is None:
            session_id = generate_computing_uuid()
        if options is None:
            options = {}
        max_workers = options.get("task_cores", None)
        self._session = Session(session_id, max_workers=max_workers)

    def get_standalone_session(self):
        return self._session

    @property
    def session_id(self):
        return self._session.session_id

    def load(self, address: AddressABC, partitions: int, schema: dict, **kwargs):
        from ...common.address import StandaloneAddress
        from ...storage import StandaloneStoreType

        if isinstance(address, StandaloneAddress):
            raw_table = self._session.load(address.name, address.namespace)
            if address.storage_type != StandaloneStoreType.ROLLPAIR_IN_MEMORY:
                raw_table = raw_table.save_as(
                    name=f"{address.name}_{uuid()}",
                    namespace=address.namespace,
                    partition=partitions,
                    need_cleanup=True,
                )
            table = Table(raw_table)
            table.schema = schema
            return table

        from ...common.address import PathAddress

        if isinstance(address, PathAddress):
            from ...computing import ComputingEngine
            from ...computing.non_distributed import LocalData

            return LocalData(address.path, engine=ComputingEngine.STANDALONE)
        raise NotImplementedError(
            f"address type {type(address)} not supported with standalone backend"
        )

    def parallelize(self, data: Iterable, partition: int, include_key: bool, **kwargs):
        table = self._session.parallelize(
            data=data, partition=partition, include_key=include_key, **kwargs
        )
        return Table(table)

    def cleanup(self, name, namespace):
        return self._session.cleanup(name=name, namespace=namespace)

    def stop(self):
        return self._session.stop()

    def kill(self):
        return self._session.kill()

    def destroy(self):
        try:
            LOGGER.info(f"clean table namespace {self.session_id}")
            self.cleanup(namespace=self.session_id, name="*")
        except Exception:
            LOGGER.warning(f"no found table namespace {self.session_id}")

        try:
            self.stop()
        except Exception as e:
            LOGGER.warning(
                f"stop storage session {self.session_id} failed, try to kill", e
            )
            self.kill()
