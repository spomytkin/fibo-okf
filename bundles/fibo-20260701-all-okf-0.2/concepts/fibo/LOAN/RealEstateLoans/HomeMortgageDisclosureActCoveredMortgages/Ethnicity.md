---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ethnicity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: category based on a cultural factors, including nationality, regional culture, ancestry, and language
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/Ethnicity
sources:
- id: fibo-source-c6feed0cf8
  resource: references/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
  sha256: c6feed0cf8f9c31063c105e293abb9e2add43152d3993dd5c4e7722d89df3473
  title: FIBO source LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
title: ethnicity
type: Ontology Class
---

# ethnicity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/Ethnicity>

## Definition

category based on a cultural factors, including nationality, regional culture, ancestry, and language

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: ethnicity
- **definition**: category based on a cultural factors, including nationality, regional culture, ancestry, and language

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
