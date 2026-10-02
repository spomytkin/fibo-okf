---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: day-count convention actual/actual ISDA
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: day-count convention that uses the actual number of days in each month and actual number of days in that year for
      calculating interest payments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: See ISDA 2006 Section 4.16(b), https://web.archive.org/web/20140913145444/http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
      for more details on the calculation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This convention accounts for days in the period based on the portion in a leap year and the portion in a non-leap
      year.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: act/365
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: act/act
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: actual/365
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: actual/actual
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-ActualActualISDA
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: day-count convention actual/actual ISDA
type: Ontology Individual
---

# day-count convention actual/actual ISDA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-ActualActualISDA>

## Definition

day-count convention that uses the actual number of days in each month and actual number of days in that year for calculating interest payments

## Annotations

- **label**: day-count convention actual/actual ISDA
- **definition**: day-count convention that uses the actual number of days in each month and actual number of days in that year for calculating interest payments
- **explanatoryNote**: See ISDA 2006 Section 4.16(b), https://web.archive.org/web/20140913145444/http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf for more details on the calculation.
- **explanatoryNote**: This convention accounts for days in the period based on the portion in a leap year and the portion in a non-leap year.
- **synonym**: act/365
- **synonym**: act/act
- **synonym**: actual/365
- **synonym**: actual/actual

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
