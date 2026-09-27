---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has instrument description
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a financial instrument or FISN to an ISO 18774-compliant instrument description, that is, a collection
      of characteristics and attributes defining a financial instrument with a maximum length up to 19 alphanumeric characters
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 18774:2015(E), Securities and related financial instruments - Financial Instrument Short Name (FISN)
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasInstrumentDescription
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: has instrument description
type: Ontology Property
---

# has instrument description

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasInstrumentDescription>

## Definition

relates a financial instrument or FISN to an ISO 18774-compliant instrument description, that is, a collection of characteristics and attributes defining a financial instrument with a maximum length up to 19 alphanumeric characters

## Relationships

- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: has instrument description
- **definition**: relates a financial instrument or FISN to an ISO 18774-compliant instrument description, that is, a collection of characteristics and attributes defining a financial instrument with a maximum length up to 19 alphanumeric characters
- **adaptedFrom**: ISO 18774:2015(E), Securities and related financial instruments - Financial Instrument Short Name (FISN)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
