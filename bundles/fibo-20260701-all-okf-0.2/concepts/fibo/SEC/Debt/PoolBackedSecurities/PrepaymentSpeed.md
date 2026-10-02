---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: prepayment speed
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: estimated rate at which a debt or part of a debt is paid off ahead of schedule
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'This is a model. Includes other factors such as homogeniety. Earlier notes: Same as Payment. Curtailment. Paydown
      is normally scheduled payments of the mortgage. Prepayment is when someone pays off the mortgage early I may send in
      1500 when my monthly amount is 1000 a month. So the 500 is a prepayment. Scheduled principal payment. More notes 25
      nov: Also factor in changes to the pool constituents where this is allowed for that kind of MBS. So we make estimates
      of how face value will will change. face value won''t change but the underlying value of the Pf changes, so eg. the
      current mortgage factor. Model update note June 2010: Detailed types of "Prepayment Speed" analytic received from thomson
      Reuters, now modeled as sub types of this term. So term origin is PSA by extension, since this is the common super class
      of 3 specific prepayment speed analytic types defined by PSA. PSA stands for Public Securities Association. Type: PSA
      gives this as numeric, however definitions imply percentage, so defined as dated percentage for now. Many data models
      use numbers which are interpreted later as percentages so this may be the case here.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A prepayment model is used to estimate the level of prepayments (speed) on a loan portfolio that will occur in
      a set period of time, given possible changes in interest rates. Understanding prepayment speed is critical in assessing
      the value of mortgage pass-through securities. Prepayment models are based on mathematical equations and usually involve
      the analysis of historical prepayment trends to predict what will happen in the future. Prepayment models are often
      used to value mortgage pools such as GNMA securities or other securitized debt products, including mortgage-backed securities
      (MBS).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: prepayment speed
type: Ontology Class
---

# prepayment speed

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed>

## Definition

estimated rate at which a debt or part of a debt is paid off ahead of schedule

## Relationships

- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [LoanPoolPrepaymentModel](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel.md)

## Annotations

- **label** (en): prepayment speed
- **definition** (en): estimated rate at which a debt or part of a debt is paid off ahead of schedule
- **editorialNote** (en): This is a model. Includes other factors such as homogeniety. Earlier notes: Same as Payment. Curtailment. Paydown is normally scheduled payments of the mortgage. Prepayment is when someone pays off the mortgage early I may send in 1500 when my monthly amount is 1000 a month. So the 500 is a prepayment. Scheduled principal payment. More notes 25 nov: Also factor in changes to the pool constituents where this is allowed for that kind of MBS. So we make estimates of how face value will will change. face value won't change but the underlying value of the Pf changes, so eg. the current mortgage factor. Model update note June 2010: Detailed types of "Prepayment Speed" analytic received from thomson Reuters, now modeled as sub types of this term. So term origin is PSA by extension, since this is the common super class of 3 specific prepayment speed analytic types defined by PSA. PSA stands for Public Securities Association. Type: PSA gives this as numeric, however definitions imply percentage, so defined as dated percentage for now. Many data models use numbers which are interpreted later as percentages so this may be the case here.
- **explanatoryNote** (en): A prepayment model is used to estimate the level of prepayments (speed) on a loan portfolio that will occur in a set period of time, given possible changes in interest rates. Understanding prepayment speed is critical in assessing the value of mortgage pass-through securities. Prepayment models are based on mathematical equations and usually involve the analysis of historical prepayment trends to predict what will happen in the future. Prepayment models are often used to value mortgage pools such as GNMA securities or other securitized debt products, including mortgage-backed securities (MBS).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
