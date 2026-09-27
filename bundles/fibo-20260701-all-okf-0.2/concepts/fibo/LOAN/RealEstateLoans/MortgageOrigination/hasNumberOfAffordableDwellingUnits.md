---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has number of affordable dwelling units
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates real estate to the number of dwelling units it contains that are income-restricted under Federal, State,
      or local affordable housing programs.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: the 2015 Revised HMDA regulation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfDwellingUnits.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfDwellingUnits
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfAffordableDwellingUnits
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: has number of affordable dwelling units
type: Ontology Property
---

# has number of affordable dwelling units

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfAffordableDwellingUnits>

## Definition

relates real estate to the number of dwelling units it contains that are income-restricted under Federal, State, or local affordable housing programs.

## Relationships

- **Subproperty of**: [hasNumberOfDwellingUnits](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfDwellingUnits.md)

## Annotations

- **label**: has number of affordable dwelling units
- **definition**: relates real estate to the number of dwelling units it contains that are income-restricted under Federal, State, or local affordable housing programs.
- **adaptedFrom**: the 2015 Revised HMDA regulation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
