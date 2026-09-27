---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has initial funding date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a mortgage to the date on which the contract is consummated, officially creating the obligations therein
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has closing date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasEffectiveDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDate
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/hasInitialFundingDate
sources:
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: has initial funding date
type: Ontology Property
---

# has initial funding date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/hasInitialFundingDate>

## Definition

relates a mortgage to the date on which the contract is consummated, officially creating the obligations therein

## Relationships

- **Subproperty of**: [hasEffectiveDate](/concepts/fibo/FND/Agreements/Contracts/hasEffectiveDate.md)

## Annotations

- **label**: has initial funding date
- **definition**: relates a mortgage to the date on which the contract is consummated, officially creating the obligations therein
- **synonym**: has closing date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
