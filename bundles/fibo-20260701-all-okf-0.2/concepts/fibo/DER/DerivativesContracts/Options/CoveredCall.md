---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: covered call
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: call option in which the seller (investor) owns an equivalent amount of the underlying security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/CallOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CoveredCall
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: covered call
type: Ontology Class
---

# covered call

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CoveredCall>

## Definition

call option in which the seller (investor) owns an equivalent amount of the underlying security

## Relationships

- **Subclass of**: [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)

## Annotations

- **label** (en): covered call
- **definition** (en): call option in which the seller (investor) owns an equivalent amount of the underlying security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
