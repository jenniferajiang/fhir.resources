# -*- coding: utf-8 -*-
"""see: https://www.hl7.org/fhir/extensibility.html
Extensibility feature for FHIR Primitive Data Types.
"""
__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError

from . import fhirabstractmodel, fhirtypes


class FHIRPrimitiveExtension(fhirabstractmodel.FHIRAbstractModel):
    """"""

    resource_type = Field("FHIRPrimitiveExtension", const=True)

    id: fhirtypes.Id = Field(
        None,
        alias="id",
        title="Type `Id`",
        description="Unique id for inter-element referencing",
        # if property is element of this resource.
        element_property=False,
    )

    extension: typing.List[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional content defined by implementations",
        # if property is element of this resource.
        element_property=True,
    )

    @root_validator(pre=True)
    def validate_extension_or_fhir_comment_required(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """Conditional Required Validation"""
        errors = list()
        extension = values.get("extension", None)
        fhir_comments = values.get("fhir_comments", None)

        if extension is None and fhir_comments is None:
            errors.append(ErrorWrapper(MissingError(), loc="extension"))
            raise ValidationError(errors, cls)  # type: ignore

        return values

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from ``FHIRPrimitiveExtension`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]
