---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit derivative
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument that is a privately held, negotiable bilateral contract traded over-the-counter (OTC) between
      two parties in a creditor/debtor relationship, enabling the creditor to effectively transfer some or all of the risk
      of a debtor defaulting to a third party
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include credit default swaps (CDS), collateralized debt obligations (CDO), total return swaps, and credit
      spread options and forwards.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The third party accepts the risk in return for payment, known as the premium.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CreditDerivative
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: credit derivative
type: Ontology Class
---

# credit derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CreditDerivative>

## Definition

derivative instrument that is a privately held, negotiable bilateral contract traded over-the-counter (OTC) between two parties in a creditor/debtor relationship, enabling the creditor to effectively transfer some or all of the risk of a debtor defaulting to a third party

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Annotations

- **label** (en): credit derivative
- **definition** (en): derivative instrument that is a privately held, negotiable bilateral contract traded over-the-counter (OTC) between two parties in a creditor/debtor relationship, enabling the creditor to effectively transfer some or all of the risk of a debtor defaulting to a third party
- **example** (en): Examples include credit default swaps (CDS), collateralized debt obligations (CDO), total return swaps, and credit spread options and forwards.
- **explanatoryNote** (en): The third party accepts the risk in return for payment, known as the premium.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
