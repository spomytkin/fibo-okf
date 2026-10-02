---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities restriction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal obligation that is applicable to a financial instrument or listing as mandated in a law or by contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
    value: Na6e983efbe0d4669a492b2816ecbeecd
  - kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: Na56579ff88914c45bb582527b53e1c3a
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: securities restriction
type: Ontology Class
---

# securities restriction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction>

## Definition

legal obligation that is applicable to a financial instrument or listing as mandated in a law or by contract

## Relationships

- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Constraints

- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: all values from value `Na6e983efbe0d4669a492b2816ecbeecd`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from value `Na56579ff88914c45bb582527b53e1c3a`

## Annotations

- **label**: securities restriction
- **definition**: legal obligation that is applicable to a financial instrument or listing as mandated in a law or by contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
