---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has principal repayment date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an instrument to the date by which the principal must be repaid in full
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Depending on the terms of the instrument (debt security, such as a bond, loan, etc.), this may be the date of a
      single payment of the debt principal or of the completion of scheduled partial redemption payments.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipalRepaymentDate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has principal repayment date
type: Ontology Property
---

# has principal repayment date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipalRepaymentDate>

## Definition

relates an instrument to the date by which the principal must be repaid in full

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Domain**: [PrincipalRepaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)

## Annotations

- **label**: has principal repayment date
- **definition**: relates an instrument to the date by which the principal must be repaid in full
- **explanatoryNote**: Depending on the terms of the instrument (debt security, such as a bond, loan, etc.), this may be the date of a single payment of the debt principal or of the completion of scheduled partial redemption payments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
