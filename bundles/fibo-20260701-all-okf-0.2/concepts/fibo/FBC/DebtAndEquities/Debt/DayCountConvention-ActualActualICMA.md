---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: day-count convention actual/actual ICMA
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: day-count convention that uses the actual number of days in each month and actual number of days in that year for
      calculating interest payments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: See ICMA Rule 251.1(iii), ISDA 2006 Section 4.16(c), https://web.archive.org/web/20140913145444/http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
      for more details on the calculation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This method ensures that all coupon payments are always for the same amount. It also ensures that all days in a
      coupon period are valued equally. This is the convention used for US Treasury bonds and notes, among other securities.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: ISMA-99
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: act/act ICMA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: act/act ISMA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: actual/actual
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-ActualActualICMA
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: day-count convention actual/actual ICMA
type: Ontology Individual
---

# day-count convention actual/actual ICMA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-ActualActualICMA>

## Definition

day-count convention that uses the actual number of days in each month and actual number of days in that year for calculating interest payments

## Annotations

- **label**: day-count convention actual/actual ICMA
- **definition**: day-count convention that uses the actual number of days in each month and actual number of days in that year for calculating interest payments
- **explanatoryNote**: See ICMA Rule 251.1(iii), ISDA 2006 Section 4.16(c), https://web.archive.org/web/20140913145444/http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf for more details on the calculation.
- **explanatoryNote**: This method ensures that all coupon payments are always for the same amount. It also ensures that all days in a coupon period are valued equally. This is the convention used for US Treasury bonds and notes, among other securities.
- **synonym**: ISMA-99
- **synonym**: act/act ICMA
- **synonym**: act/act ISMA
- **synonym**: actual/actual

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
