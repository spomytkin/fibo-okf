"""Reusable RDF/OWL to OKF 0.2 compiler with ontology profiles."""

__version__ = "0.1.0"

from .compiler import compile_ontology

__all__ = ["compile_ontology", "__version__"]
