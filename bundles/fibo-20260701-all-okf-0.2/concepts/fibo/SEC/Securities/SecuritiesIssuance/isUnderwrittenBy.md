---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is underwritten by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an offering to an underwriter involved in raising capital for or distributing the instruments that are
      the subject of the offering
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: is underwritten by
type: Ontology Property
---

# is underwritten by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy>

## Definition

relates an offering to an underwriter involved in raising capital for or distributing the instruments that are the subject of the offering

## Relationships

- **Domain**: [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)
- **Range**: [Underwriter](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)

## Annotations

- **label**: is underwritten by
- **definition**: relates an offering to an underwriter involved in raising capital for or distributing the instruments that are the subject of the offering

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
