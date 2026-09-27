---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket of credit risks
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of instruments, legal entities, or a combination thereof collected for the purpose of analyzing risk
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the risk related to a given constituent may be calculated based on either (1) the overall credit risk
      associated with the entity or, (2) the combined risk associated with an entity and the specific instrument identified,
      or (3) risk associated with the instrument on its own. Criteria for constituents is based on sectors (emerging market,
      financial, sovereign, etc), spread range (investment grade, non-investment grade), or asset type (loan, bond, mortgage-backed,
      asset-backed), second criteria is based on maturity of protection (2,3,5,7,10 yrs). Markit manages over 2000 CDS indexes,
      for example.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndexConstituent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfCreditRisks
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: basket of credit risks
type: Ontology Class
---

# basket of credit risks

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfCreditRisks>

## Definition

basket of instruments, legal entities, or a combination thereof collected for the purpose of analyzing risk

## Relationships

- **Subclass of**: [WeightedBasket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [CreditIndexConstituent](/concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndexConstituent.md)

## Annotations

- **label** (en): basket of credit risks
- **definition** (en): basket of instruments, legal entities, or a combination thereof collected for the purpose of analyzing risk
- **explanatoryNote** (en): Note that the risk related to a given constituent may be calculated based on either (1) the overall credit risk associated with the entity or, (2) the combined risk associated with an entity and the specific instrument identified, or (3) risk associated with the instrument on its own. Criteria for constituents is based on sectors (emerging market, financial, sovereign, etc), spread range (investment grade, non-investment grade), or asset type (loan, bond, mortgage-backed, asset-backed), second criteria is based on maturity of protection (2,3,5,7,10 yrs). Markit manages over 2000 CDS indexes, for example.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
