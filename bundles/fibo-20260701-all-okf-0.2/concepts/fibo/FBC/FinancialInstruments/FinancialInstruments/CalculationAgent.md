---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calculation agent
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is responsible for determining the value of an instrument and in some cases, determines how much the
      parties owe one another
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A calculation agent is an entity responsible for performing calculations and determinations outlined in financial
      agreements, often related to derivatives or structured products. They ensure accuracy and timeliness in calculating
      payments, interest rates, or other terms based on predefined formulas and market conditions. The agent can establish
      the price for a given instrument and may act as its guarantor and issuer. If the counterparty in a derivative transaction
      is a broker-dealer, then the broker-dealer will often act as the calculation agent.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: calculation agent
type: Ontology Class
---

# calculation agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent>

## Definition

party that is responsible for determining the value of an instrument and in some cases, determines how much the parties owe one another

## Relationships

- **Subclass of**: [ThirdPartyAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)

## Annotations

- **label** (en): calculation agent
- **definition** (en): party that is responsible for determining the value of an instrument and in some cases, determines how much the parties owe one another
- **explanatoryNote** (en): A calculation agent is an entity responsible for performing calculations and determinations outlined in financial agreements, often related to derivatives or structured products. They ensure accuracy and timeliness in calculating payments, interest rates, or other terms based on predefined formulas and market conditions. The agent can establish the price for a given instrument and may act as its guarantor and issuer. If the counterparty in a derivative transaction is a broker-dealer, then the broker-dealer will often act as the calculation agent.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
