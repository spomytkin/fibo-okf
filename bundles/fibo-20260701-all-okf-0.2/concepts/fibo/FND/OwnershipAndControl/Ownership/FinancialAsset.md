---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-physical, tangible asset whose value is derived from a contractual claim, such as bank deposits, bonds, stocks,
      rights, certificates, and bank balances
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Financial assets are typically more liquid than other tangible assets, such as commodities or real estate. Financial
      assets may not cover all assets that might be included on a balance sheet, and do not include tangible, physical assets
      or intangible assets such as intellectual property.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasAcquisitionPrice
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/TangibleAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/TangibleAsset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: financial asset
type: Ontology Class
---

# financial asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset>

## Definition

non-physical, tangible asset whose value is derived from a contractual claim, such as bank deposits, bonds, stocks, rights, certificates, and bank balances

## Relationships

- **Subclass of**: [TangibleAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/TangibleAsset.md)

## Constraints

- **[hasAcquisitionPrice](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasAcquisitionPrice.md)**: all values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Annotations

- **label**: financial asset
- **definition**: non-physical, tangible asset whose value is derived from a contractual claim, such as bank deposits, bonds, stocks, rights, certificates, and bank balances
- **explanatoryNote**: Financial assets are typically more liquid than other tangible assets, such as commodities or real estate. Financial assets may not cover all assets that might be included on a balance sheet, and do not include tangible, physical assets or intangible assets such as intellectual property.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
