---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: initial margin
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: money or securities put up as a good faith deposit assuring that a future contract will be fulfilled
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'When you open a futures contract, the futures exchange will state a minimum amount of money that you must deposit
      into your account. This original deposit of money is called the initial margin. When your contract is liquidated, you
      will be refunded the initial margin plus or minus any gains or losses that occur over the span of the futures contract.
      In other words, the amount in your margin account changes daily as the market fluctuates in relation to your futures
      contract. The minimum-level margin is determined by the futures exchange and is usually 5% to 10% of the futures contract.
      These predetermined initial margin amounts are continuously under review: at times of high market volatility, initial
      margin requirements can be raised.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: security deposit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/InitialMargin
sources:
- id: fibo-source-c2e233cb71
  resource: references/fibo/MD/DerivativesTemporal/FuturesTemporal.rdf
  sha256: c2e233cb71a6057762c1da19bf2b1316166cd651fcf570e55af51b91c70f41c5
  title: FIBO source MD/DerivativesTemporal/FuturesTemporal.rdf
title: initial margin
type: Ontology Class
---

# initial margin

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/InitialMargin>

## Definition

money or securities put up as a good faith deposit assuring that a future contract will be fulfilled

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Constraints

- **[hasAsOfDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAsOfDate.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: some values from of type [FuturesTradingAccountHolder](/concepts/fibo/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder.md)

## Annotations

- **label** (en): initial margin
- **definition** (en): money or securities put up as a good faith deposit assuring that a future contract will be fulfilled
- **explanatoryNote** (en): When you open a futures contract, the futures exchange will state a minimum amount of money that you must deposit into your account. This original deposit of money is called the initial margin. When your contract is liquidated, you will be refunded the initial margin plus or minus any gains or losses that occur over the span of the futures contract. In other words, the amount in your margin account changes daily as the market fluctuates in relation to your futures contract. The minimum-level margin is determined by the futures exchange and is usually 5% to 10% of the futures contract. These predetermined initial margin amounts are continuously under review: at times of high market volatility, initial margin requirements can be raised.
- **synonym** (en): security deposit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
