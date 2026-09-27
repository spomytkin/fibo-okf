---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ratio debt basket
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of debt instruments whose constituents are specified based on a leverage ratio based on total debt rather
      than only secured debt
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The ratio basket provides different ratio tests depending on the type of indebtedness being incurred (for example,
      first lien leverage ratio in respect of first lien indebtedness, senior secured leverage ratio in respect of indebtedness
      secured by a junior lien and a total net leverage ratio or interest coverage ratio in respect of unsecured indebtedness).
      A ratio basket would typically allow the borrower to incur debt secured on a senior secured basis subject to a maximum
      senior secured leverage ratio and unsecured debt subject to a maximum total leverage ratio.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/RatioDebtBasket
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: ratio debt basket
type: Ontology Class
---

# ratio debt basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/RatioDebtBasket>

## Definition

basket of debt instruments whose constituents are specified based on a leverage ratio based on total debt rather than only secured debt

## Relationships

- **Subclass of**: [BasketOfDebtInstruments](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md)

## Annotations

- **label** (en): ratio debt basket
- **definition** (en): basket of debt instruments whose constituents are specified based on a leverage ratio based on total debt rather than only secured debt
- **explanatoryNote** (en): The ratio basket provides different ratio tests depending on the type of indebtedness being incurred (for example, first lien leverage ratio in respect of first lien indebtedness, senior secured leverage ratio in respect of indebtedness secured by a junior lien and a total net leverage ratio or interest coverage ratio in respect of unsecured indebtedness). A ratio basket would typically allow the borrower to incur debt secured on a senior secured basis subject to a maximum senior secured leverage ratio and unsecured debt subject to a maximum total leverage ratio.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
