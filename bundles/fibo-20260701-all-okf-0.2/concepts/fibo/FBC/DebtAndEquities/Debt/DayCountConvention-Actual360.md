---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: day-count convention actual/360
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: day-count convention that uses the actual number of days in each month and 360 days in a year for calculating interest
      payments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: See ICMA Rule 251.1(i) (not sterling), ISDA 2006 Section 4.16(e), https://web.archive.org/web/20140913145444/http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
      for more details on the calculation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This convention is used in money markets for short-term lending of currencies, including the US dollar and Euro,
      and is applied in ESCB monetary policy operations. It is the convention used with repurchase agreements.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: French
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: a/360
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: act/360
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-Actual360
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: day-count convention actual/360
type: Ontology Individual
---

# day-count convention actual/360

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-Actual360>

## Definition

day-count convention that uses the actual number of days in each month and 360 days in a year for calculating interest payments

## Annotations

- **label**: day-count convention actual/360
- **definition**: day-count convention that uses the actual number of days in each month and 360 days in a year for calculating interest payments
- **explanatoryNote**: See ICMA Rule 251.1(i) (not sterling), ISDA 2006 Section 4.16(e), https://web.archive.org/web/20140913145444/http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf for more details on the calculation.
- **explanatoryNote**: This convention is used in money markets for short-term lending of currencies, including the US dollar and Euro, and is applied in ESCB monetary policy operations. It is the convention used with repurchase agreements.
- **synonym**: French
- **synonym**: a/360
- **synonym**: act/360

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
