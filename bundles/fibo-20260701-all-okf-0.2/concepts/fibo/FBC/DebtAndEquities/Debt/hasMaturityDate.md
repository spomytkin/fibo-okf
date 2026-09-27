---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has maturity date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date on which the principal amount of an instrument is due to be repaid to the investor and interest
      or coupon payments stop, and/or the date on which the instrument may be redeemed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Maturity dates typically apply to debt instruments, such as notes, drafts, bonds, and other loans, but may also
      apply to preferred shares and other financial instruments.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaturityDate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has maturity date
type: Ontology Property
---

# has maturity date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaturityDate>

## Definition

indicates the date on which the principal amount of an instrument is due to be repaid to the investor and interest or coupon payments stop, and/or the date on which the instrument may be redeemed

## Relationships

- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has maturity date
- **definition**: indicates the date on which the principal amount of an instrument is due to be repaid to the investor and interest or coupon payments stop, and/or the date on which the instrument may be redeemed
- **explanatoryNote**: Maturity dates typically apply to debt instruments, such as notes, drafts, bonds, and other loans, but may also apply to preferred shares and other financial instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
