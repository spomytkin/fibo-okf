---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has originator person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something, typically a loan, to a person that initially originates or creates it
  range:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasParty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatorPerson
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: has originator person
type: Ontology Property
---

# has originator person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatorPerson>

## Definition

relates something, typically a loan, to a person that initially originates or creates it

## Relationships

- **Range**: [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
- **Subproperty of**: [hasParty](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasParty>)

## Annotations

- **label**: has originator person
- **definition**: relates something, typically a loan, to a person that initially originates or creates it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
