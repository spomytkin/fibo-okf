---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: leveraged product
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured product that provides a further enhanced yield (over and above that of a yield-enhancement product),
      often without any limit to the upside participation, and frequently with a stop-loss in order to limit potential capital
      losses
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Leveraged certificates are examples of leveraged products; they provide enhanced participation to an underlying
      with inbuilt leverage. Leveraged exposure is also provided on the downside performance of the underlying. Another example
      is a call warrant, which is simply a call option that is traded in a securitized format. This format is interesting
      in order to be able to trade a call option on underlyings for which no exchange traded option market exists.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/LeveragedProduct
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: leveraged product
type: Ontology Class
---

# leveraged product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/LeveragedProduct>

## Definition

structured product that provides a further enhanced yield (over and above that of a yield-enhancement product), often without any limit to the upside participation, and frequently with a stop-loss in order to limit potential capital losses

## Relationships

- **Subclass of**: [StructuredProduct](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)

## Annotations

- **label** (en): leveraged product
- **definition** (en): structured product that provides a further enhanced yield (over and above that of a yield-enhancement product), often without any limit to the upside participation, and frequently with a stop-loss in order to limit potential capital losses
- **example** (en): Leveraged certificates are examples of leveraged products; they provide enhanced participation to an underlying with inbuilt leverage. Leveraged exposure is also provided on the downside performance of the underlying. Another example is a call warrant, which is simply a call option that is traded in a securitized format. This format is interesting in order to be able to trade a call option on underlyings for which no exchange traded option market exists.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
