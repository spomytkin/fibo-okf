---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument short name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: abbreviated name for a financial instrument within a defined structure as specified in ISO 18774
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FISN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 18774:2015(E), Securities and related financial instruments - Financial Instrument Short Name (FISN)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasInstrumentDescription
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasIssuerShortName
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/FinancialInstrumentShortName
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: financial instrument short name
type: Ontology Class
---

# financial instrument short name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/FinancialInstrumentShortName>

## Definition

abbreviated name for a financial instrument within a defined structure as specified in ISO 18774

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[hasInstrumentDescription](/concepts/fibo/SEC/Securities/SecuritiesIssuance/hasInstrumentDescription.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasIssuerShortName](/concepts/fibo/SEC/Securities/SecuritiesIssuance/hasIssuerShortName.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: financial instrument short name
- **definition**: abbreviated name for a financial instrument within a defined structure as specified in ISO 18774
- **abbreviation**: FISN
- **adaptedFrom**: ISO 18774:2015(E), Securities and related financial instruments - Financial Instrument Short Name (FISN)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
