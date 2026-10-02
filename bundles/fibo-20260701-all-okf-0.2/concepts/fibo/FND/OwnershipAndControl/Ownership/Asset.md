---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: something of monetary value that is owned or provides benefit to some party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Financial Accounting Standards Board (FASB) Statement of Financial Accounting Concepts No. 6, Elements of Financial
      Statements, paragraph 25.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'An asset is something that provides probable future economic benefit obtained or controlled by some party as a
      result of past transactions or events. An asset has three essential characteristics: (a) it embodies a probable future
      benefit that involves a capacity, singly or in combination with other assets, to contribute directly or indirectly to
      future net cash inflows, (b) a party can obtain the benefit and control others'' access to it, and (c) the transaction
      or other event giving rise to the party''s right to or control of the benefit has already occurred.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: economic resource
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAcquisitionDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Price
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasAcquisitionPrice
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isAssetOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwnedAsset
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Undergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: asset
type: Ontology Class
---

# asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset>

## Definition

something of monetary value that is owned or provides benefit to some party

## Relationships

- **Subclass of**: [Undergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/Undergoer>)

## Constraints

- **[hasAcquisitionDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAcquisitionDate.md)**: exact qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasAcquisitionPrice](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasAcquisitionPrice.md)**: max qualified cardinality 1 of type [Price](/concepts/fibo/FND/Accounting/CurrencyAmount/Price.md)
- **[isAssetOf](/concepts/fibo/FND/OwnershipAndControl/Ownership/isAssetOf.md)**: some values from of type [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)
- **[isOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/isOwnedAsset.md)**: some values from of type [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)

## Annotations

- **label**: asset
- **definition**: something of monetary value that is owned or provides benefit to some party
- **adaptedFrom**: Financial Accounting Standards Board (FASB) Statement of Financial Accounting Concepts No. 6, Elements of Financial Statements, paragraph 25.
- **explanatoryNote**: An asset is something that provides probable future economic benefit obtained or controlled by some party as a result of past transactions or events. An asset has three essential characteristics: (a) it embodies a probable future benefit that involves a capacity, singly or in combination with other assets, to contribute directly or indirectly to future net cash inflows, (b) a party can obtain the benefit and control others' access to it, and (c) the transaction or other event giving rise to the party's right to or control of the benefit has already occurred.
- **synonym**: economic resource

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
