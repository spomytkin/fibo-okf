---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CLDR
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: calendar
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Calendar defines the non-working days which affect the dates of contract events (CDE's) in combination with EOMC
      and BDC. Custom calendars can be added as additional enum options.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CLDR
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Calendar
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CLDR
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CLDR
type: Ontology Individual
---

# ACTUS contract term - CLDR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CLDR>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Calendar](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar.md)

## Annotations

- **label**: ACTUS contract term - CLDR
- **hasParameterName**: calendar
- **hasDescription**: Calendar defines the non-working days which affect the dates of contract events (CDE's) in combination with EOMC and BDC. Custom calendars can be added as additional enum options.
- **hasTag**: CLDR
- **hasTextualName**: Calendar

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
