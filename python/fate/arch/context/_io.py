from typing import Protocol

from ..unify import URI


class IOKit:
    @staticmethod
    def _parse_args(arg, **kwargs):
        name = ""
        metadata = {}
        if hasattr(arg, "uri"):
            uri = arg.uri
            name = arg.name
            metadata = arg.metadata
        elif isinstance(arg[0], str):
            uri = arg[0]
        else:
            raise ValueError(f"invalid arguments: {arg} and {kwargs}")
        if "name" in kwargs:
            name = kwargs["name"]
        if "metadata" in kwargs:
            metadata = kwargs["metadata"]
        for k, v in kwargs.items():
            if k not in ["name", "metadata"]:
                metadata[k] = v

        uri = URI.from_string(uri)
        format = metadata.get("format")
        return format, name, uri, metadata

    def reader(self, ctx, arg, **kwargs) -> "Reader":
        format, name, uri, metadata = self._parse_args(arg, **kwargs)
        if format is None:
            raise ValueError(f"reader format `{format}` unknown")
        return get_reader(format, ctx, name, uri, metadata)

    def writer(self, ctx, arg, **kwargs) -> "Writer":
        format, name, uri, metadata = self._parse_args(arg, **kwargs)
        if format is None:
            raise ValueError(f"reader format `{format}` unknown")
        return get_writer(format, ctx, name, uri, metadata)


class Reader(Protocol):
    def read_dataframe(self):
        ...


def get_reader(format, ctx, name, uri, metadata) -> Reader:
    if format == "csv":
        return CSVReader(ctx, name, uri.path, metadata)

    if format == "json":
        return JsonReader(ctx, name, uri.path, metadata)

    raise ValueError(f"reader for format {format} not found")


class CSVReader:
    def __init__(self, ctx, name: str, uri: URI, metadata: dict) -> None:
        self.name = name
        self.ctx = ctx
        self.uri = uri
        self.metadata = metadata

    def read_dataframe(self):
        import inspect

        from fate.arch import dataframe

        kwargs = {}
        p = inspect.signature(dataframe.CSVReader.__init__).parameters
        parameter_keys = p.keys()
        for k, v in self.metadata.items():
            if k in parameter_keys:
                kwargs[k] = v

        dataframe_reader = dataframe.CSVReader(**kwargs).to_frame(self.ctx, self.uri)
        return DataframeReader(dataframe_reader, self.metadata["num_features"], self.metadata["num_samples"])


class JsonReader:
    def __init__(self, ctx, name: str, uri, metadata: dict) -> None:
        self.name = name
        self.ctx = ctx
        self.uri = uri
        self.metadata = metadata

    def read_model(self):
        import json

        with open(self.uri, "r") as f:
            return json.load(f)

    def read_metric(self):
        import json

        with open(self.uri, "r") as f:
            return json.load(f)


class DataframeReader:
    def __init__(self, frames, num_features, num_samples) -> None:
        self.data = frames
        self.num_features = num_features
        self.num_samples = num_samples

    def __len__(self):
        return self.num_samples

    def to_local(self):
        return self.data.to_local()


class LibSVMReader:
    def read(self):
        ...

    def read_dataframe(self):
        ...


def get_writer(format, ctx, name, uri, metadata) -> Reader:
    if format == "csv":
        return CSVWriter(ctx, name, uri, metadata)

    if format == "json":
        return JsonWriter(ctx, name, uri.path, metadata)

    raise ValueError(f"wirter for format {format} not found")


class Writer(Protocol):
    ...


class CSVWriter:
    def __init__(self, ctx, name: str, uri: URI, metadata: dict) -> None:
        self.name = name
        self.ctx = ctx
        self.uri = uri
        self.metadata = metadata

    def write_dataframe(self, df):
        ...


class JsonWriter:
    def __init__(self, ctx, name: str, uri, metadata: dict) -> None:
        self.name = name
        self.ctx = ctx
        self.uri = uri
        self.metadata = metadata

    def write_model(self, model):
        import json

        with open(self.uri, "w") as f:
            json.dump(model, f)

    def write_metric(self, metric):
        import json

        with open(self.uri, "w") as f:
            json.dump(metric, f)


class LibSVMWriter:
    ...
