---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket of credit default swaps
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of reference obligations are credit default swap instruments
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the CDS Index is broken down into tranches depending on different types of credits, for example, investment
      grade and high yield. Tranches are defined by attachment and detachment points for the index loss distribution. It means
      that when default events occur the lower-level tranches absorb the loss up to the detachment point, before moving to
      the next senior tranche.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: basket of credit default swaps
type: Ontology Class
---

# basket of credit default swaps

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps>

## Definition

basket of reference obligations are credit default swap instruments

## Relationships

- **Subclass of**: [WeightedBasket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [CreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)

## Annotations

- **label** (en): basket of credit default swaps
- **definition** (en): basket of reference obligations are credit default swap instruments
- **explanatoryNote** (en): Note that the CDS Index is broken down into tranches depending on different types of credits, for example, investment grade and high yield. Tranches are defined by attachment and detachment points for the index loss distribution. It means that when default events occur the lower-level tranches absorb the loss up to the detachment point, before moving to the next senior tranche.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
