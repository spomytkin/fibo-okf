---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: asset-backed credit default swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit default swap whose underlying reference obligation is an asset-backed security rather than corporate credit
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ABCDS
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the case of an ABCDS, the buyer receives protection for defaults on asset-backed securities or tranches of securities,
      rather than protecting against the default of a particular issuer. Asset-backed securities are securities backed by
      a pool of loans or receivables, such as auto loans, home equity loans or credit cards loans.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/AssetBackedCreditDefaultSwap
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: asset-backed credit default swap
type: Ontology Class
---

# asset-backed credit default swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/AssetBackedCreditDefaultSwap>

## Definition

credit default swap whose underlying reference obligation is an asset-backed security rather than corporate credit

## Relationships

- **Subclass of**: [CreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)

## Annotations

- **label** (en): asset-backed credit default swap
- **definition** (en): credit default swap whose underlying reference obligation is an asset-backed security rather than corporate credit
- **abbreviation** (en): ABCDS
- **explanatoryNote** (en): In the case of an ABCDS, the buyer receives protection for defaults on asset-backed securities or tranches of securities, rather than protecting against the default of a particular issuer. Asset-backed securities are securities backed by a pool of loans or receivables, such as auto loans, home equity loans or credit cards loans.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
