---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bill of exchange
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: short-term negotiable financial instrument consisting of an order in writing addressed by one person (the seller
      of goods) to another (the buyer), requiring the latter to pay a fixed amount of money on demand (a sight draft) or on
      a predetermined date (a time draft)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A bill of exchange is a written agreement between two parties - the buyer and the seller - used primarily in international
      trade. The buyer or seller typically employs a bank to issue the bill of exchange due to the risks involved with international
      transactions. Bills of exchange can be transferred by endorsement, much like a check. They can also require the buyer
      to pay a third party - a bank - in the event that the buyer fails to make good on his agreement with the seller.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bank draft
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: draft
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payee
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/Drawee
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/Drawer
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BillOfExchange
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: bill of exchange
type: Ontology Class
---

# bill of exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BillOfExchange>

## Definition

short-term negotiable financial instrument consisting of an order in writing addressed by one person (the seller of goods) to another (the buyer), requiring the latter to pay a fixed amount of money on demand (a sight draft) or on a predetermined date (a time draft)

## Relationships

- **Subclass of**: [MoneyMarketInstrument](/concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: min qualified cardinality 0 of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: min qualified cardinality 0 of type [Payee](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Drawee](/concepts/fibo/SEC/Debt/TradedShortTermDebt/Drawee.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Drawer](/concepts/fibo/SEC/Debt/TradedShortTermDebt/Drawer.md)

## Annotations

- **label** (en): bill of exchange
- **definition** (en): short-term negotiable financial instrument consisting of an order in writing addressed by one person (the seller of goods) to another (the buyer), requiring the latter to pay a fixed amount of money on demand (a sight draft) or on a predetermined date (a time draft)
- **explanatoryNote** (en): A bill of exchange is a written agreement between two parties - the buyer and the seller - used primarily in international trade. The buyer or seller typically employs a bank to issue the bill of exchange due to the risks involved with international transactions. Bills of exchange can be transferred by endorsement, much like a check. They can also require the buyer to pay a third party - a bank - in the event that the buyer fails to make good on his agreement with the seller.
- **synonym** (en): bank draft
- **synonym** (en): draft

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
