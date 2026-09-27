---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European Central Bank business day adjustment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: business day adjustment for the ECB
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasBusinessCenter
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayModifiedFollowing.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayModifiedFollowing
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/EuropeanCentralBankBBusinessDayAdjustment
sources:
- id: fibo-source-dbb6868e12
  resource: references/fibo/EXMP/Securities/IRSwapExamples.rdf
  sha256: dbb6868e124bba0f62a80f6387c9e212e8d2931ed572f2e411e31534e2edcfc5
  title: FIBO source EXMP/Securities/IRSwapExamples.rdf
title: European Central Bank business day adjustment
type: Ontology Individual
---

# European Central Bank business day adjustment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/EuropeanCentralBankBBusinessDayAdjustment>

## Definition

business day adjustment for the ECB

## Relationships

- **Related to**: [BusinessDayModifiedFollowing](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayModifiedFollowing.md)
- **Related to**: [Frankfurt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md)

## Annotations

- **label**: European Central Bank business day adjustment
- **definition**: business day adjustment for the ECB

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
