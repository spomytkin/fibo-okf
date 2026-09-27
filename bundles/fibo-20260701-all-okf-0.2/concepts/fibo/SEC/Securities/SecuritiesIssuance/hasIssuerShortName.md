---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has issuer short name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a security issuer or FISN to an ISO 18774-compliant issuer short name, that is, an abbreviation of the
      official issuer name, limited to a maximum of 15 alphanumeric characters
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 18774:2015(E), Securities and related financial instruments - Financial Instrument Short Name (FISN)
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/hasFormalName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasIssuerShortName
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: has issuer short name
type: Ontology Property
---

# has issuer short name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasIssuerShortName>

## Definition

relates a security issuer or FISN to an ISO 18774-compliant issuer short name, that is, an abbreviation of the official issuer name, limited to a maximum of 15 alphanumeric characters

## Relationships

- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)
- **Subproperty of**: [hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)

## Annotations

- **label**: has issuer short name
- **definition**: relates a security issuer or FISN to an ISO 18774-compliant issuer short name, that is, an abbreviation of the official issuer name, limited to a maximum of 15 alphanumeric characters
- **adaptedFrom**: ISO 18774:2015(E), Securities and related financial instruments - Financial Instrument Short Name (FISN)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
