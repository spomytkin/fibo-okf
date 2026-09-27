---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: put feature
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: redemption provision giving the holder the right, but not the obligation, to sell a specified amount of the debt
      instrument (i.e., redeem it), prior to maturity
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: FIBIM has term "Putable Date" which (by implication, and comparing with definition for "Next Call Date") is presumably
      a single calendar date in the future, at a given point in time. That does not cover the definition of formal terms defining
      when and how the issue may be put, which is what is modeled here.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: put provision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isMandatory
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutNotificationProvision
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasNotificationProvision
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutSchedule
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: put feature
type: Ontology Class
---

# put feature

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature>

## Definition

redemption provision giving the holder the right, but not the obligation, to sell a specified amount of the debt instrument (i.e., redeem it), prior to maturity

## Relationships

- **Subclass of**: [DebtTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md)
- **Subclass of**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)

## Constraints

- **[isMandatory](/concepts/fibo/SEC/Debt/Bonds/isMandatory.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasNotificationProvision](/concepts/fibo/SEC/Debt/DebtInstruments/hasNotificationProvision.md)**: min qualified cardinality 0 of type [PutNotificationProvision](/concepts/fibo/SEC/Debt/DebtInstruments/PutNotificationProvision.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [PutSchedule](/concepts/fibo/SEC/Debt/DebtInstruments/PutSchedule.md)

## Annotations

- **label**: put feature
- **definition**: redemption provision giving the holder the right, but not the obligation, to sell a specified amount of the debt instrument (i.e., redeem it), prior to maturity
- **editorialNote**: FIBIM has term "Putable Date" which (by implication, and comparing with definition for "Next Call Date") is presumably a single calendar date in the future, at a given point in time. That does not cover the definition of formal terms defining when and how the issue may be put, which is what is modeled here.
- **synonym**: put provision

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
