---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has initial exchange date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the specific date when the initial exchange of assets or funds takes place
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IED
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For a credit agreement, this is the initial funding date, such as the funding of the principal amount, or a portion
      thereof, but for other kinds of instruments, it may be something else. In the context of contracts related to swaps,
      options, or other derivative instruments, the initial exchange date marks the point where the parties legally commit
      to the terms of the agreement and exchange the initial required amounts.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialExchangeDate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has initial exchange date
type: Ontology Property
---

# has initial exchange date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialExchangeDate>

## Definition

indicates the specific date when the initial exchange of assets or funds takes place

## Relationships

- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)
- **Subproperty of**: [hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)

## Annotations

- **label**: has initial exchange date
- **definition**: indicates the specific date when the initial exchange of assets or funds takes place
- **abbreviation**: IED
- **explanatoryNote**: For a credit agreement, this is the initial funding date, such as the funding of the principal amount, or a portion thereof, but for other kinds of instruments, it may be something else. In the context of contracts related to swaps, options, or other derivative instruments, the initial exchange date marks the point where the parties legally commit to the terms of the agreement and exchange the initial required amounts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
