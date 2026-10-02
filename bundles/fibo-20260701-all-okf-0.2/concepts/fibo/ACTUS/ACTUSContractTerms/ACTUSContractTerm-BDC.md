---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - BDC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: businessDayConvention
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'BDC''s are linked to a calendar. Calendars have working and non-working days. A BDC value other than N means that
      cash flows cannot fall on non-working days, they must be shifted to the next business day (following) or the previous
      on (preceding).


      These two simple rules get refined twofold:


      - Following modified (preceding): Same like following (preceding), however if a cash flow gets shifted into a new month,
      then it is shifted to preceding (following) business day.


      - Shift/calculate (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by
      this choice. In the case of SC first the dates are shifted and after the shift cash flows are calculated. In the case
      of CS it is the other way round.


      Attention: Does not affect non-cyclical dates such as PRD, MD, TD, IPCED since they can be set to the correct date directly.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: BDC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Business Day Convention
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-BDC
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - BDC
type: Ontology Individual
---

# ACTUS contract term - BDC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-BDC>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Calendar](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Calendar.md)

## Annotations

- **label**: ACTUS contract term - BDC
- **hasParameterName**: businessDayConvention
- **hasDescription**: BDC's are linked to a calendar. Calendars have working and non-working days. A BDC value other than N means that cash flows cannot fall on non-working days, they must be shifted to the next business day (following) or the previous on (preceding).  These two simple rules get refined twofold:  - Following modified (preceding): Same like following (preceding), however if a cash flow gets shifted into a new month, then it is shifted to preceding (following) business day.  - Shift/calculate (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by this choice. In the case of SC first the dates are shifted and after the shift cash flows are calculated. In the case of CS it is the other way round.  Attention: Does not affect non-cyclical dates such as PRD, MD, TD, IPCED since they can be set to the correct date directly.
- **hasTag**: BDC
- **hasTextualName**: Business Day Convention

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
