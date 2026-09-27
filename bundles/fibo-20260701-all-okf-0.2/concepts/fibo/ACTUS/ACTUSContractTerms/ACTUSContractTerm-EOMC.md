---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - EOMC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: endOfMonthConvention
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "When computing schedules a special problem arises if an anchor date is at the end of a month and a cycle of monthly\
      \ or quarterly is applied (yearly in the case of leap years only). How do we have to interpret an anchor date April\
      \ 30 plus 1M cycles? In case where EOM is selected, it will jump to the 31st of May, then June 30, July 31 and so on.\
      \ If SM is selected, it will jump to the 30st always with of course an exception in February. \n\nThis logic applies\
      \ for all months having 30 or less days and an anchor date at the last day. Month with 31 days will at any rate jump\
      \ to the last of the month if anchor date is on the last day."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: EOMC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: End Of Month Convention
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-EOMC
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - EOMC
type: Ontology Individual
---

# ACTUS contract term - EOMC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-EOMC>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Calendar](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar.md)

## Annotations

- **label**: ACTUS contract term - EOMC
- **hasParameterName**: endOfMonthConvention
- **hasDescription**: When computing schedules a special problem arises if an anchor date is at the end of a month and a cycle of monthly or quarterly is applied (yearly in the case of leap years only). How do we have to interpret an anchor date April 30 plus 1M cycles? In case where EOM is selected, it will jump to the 31st of May, then June 30, July 31 and so on. If SM is selected, it will jump to the 30st always with of course an exception in February.   This logic applies for all months having 30 or less days and an anchor date at the last day. Month with 31 days will at any rate jump to the last of the month if anchor date is on the last day.
- **hasTag**: EOMC
- **hasTextualName**: End Of Month Convention

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
