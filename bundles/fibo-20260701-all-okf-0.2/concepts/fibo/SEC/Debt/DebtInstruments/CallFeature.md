---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call feature
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: redemption provision defining the rights of the issuer to buy back a security at a call price after a call protection
      period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most corporate and municipal bonds have ten-year call features (termed call protection by holders); government
      securities typically have none.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: call provision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallNotificationProvision
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasNotificationProvision
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallSchedule
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: call feature
type: Ontology Class
---

# call feature

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature>

## Definition

redemption provision defining the rights of the issuer to buy back a security at a call price after a call protection period

## Relationships

- **Subclass of**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)

## Constraints

- **[hasNotificationProvision](/concepts/fibo/SEC/Debt/DebtInstruments/hasNotificationProvision.md)**: min qualified cardinality 0 of type [CallNotificationProvision](/concepts/fibo/SEC/Debt/DebtInstruments/CallNotificationProvision.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [CallSchedule](/concepts/fibo/SEC/Debt/DebtInstruments/CallSchedule.md)

## Annotations

- **label**: call feature
- **definition**: redemption provision defining the rights of the issuer to buy back a security at a call price after a call protection period
- **explanatoryNote**: Most corporate and municipal bonds have ten-year call features (termed call protection by holders); government securities typically have none.
- **synonym**: call provision

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
