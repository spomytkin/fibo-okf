---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: merchant category code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code used internationally to classify a merchant
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MCC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 18245:2003 Retail financial services - Merchant category codes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Merchant categories are organized by the type of business, trade or services supplied. Certain category codes including
      those for very large businesses, such as airlines and some hotel chains, may be delineated to the point of identifying
      the business. Merchant category codes and/or the descriptions of the service categories are frequently used in credit
      card and other banking transactions for analysis, transaction classification, such as for use in promotional rewards,
      and sometimes tax-related purposes.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Values are specified only for those merchant categories that are generally expected to originate retail financial
      transactions. Criteria for establishing a new category code includes (a) the merchant category is reasonable and substantially
      different from all other merchant categories currently represented in the list of code values; (b) the merchant category
      is separate and distinct from all other industries currently represented in the list of code values; (c) the proposal
      describes a merchant category or industry, and not a process; (d) the minimum annual sales volume of merchants included
      in the merchant category, taken as a whole, is USD 10 million; and (e) sufficient justification for the addition of
      a new code value is found.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/hasMerchantCategoryDescription
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Merchant
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCodeScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: merchant category code
type: Ontology Class
---

# merchant category code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode>

## Definition

code used internationally to classify a merchant

## Relationships

- **Subclass of**: [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[hasMerchantCategoryDescription](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/hasMerchantCategoryDescription.md)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Merchant](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/Merchant.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [MerchantCategoryCodeScheme](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCodeScheme.md)

## Annotations

- **label**: merchant category code
- **definition**: code used internationally to classify a merchant
- **abbreviation**: MCC
- **adaptedFrom**: ISO 18245:2003 Retail financial services - Merchant category codes
- **explanatoryNote**: Merchant categories are organized by the type of business, trade or services supplied. Certain category codes including those for very large businesses, such as airlines and some hotel chains, may be delineated to the point of identifying the business. Merchant category codes and/or the descriptions of the service categories are frequently used in credit card and other banking transactions for analysis, transaction classification, such as for use in promotional rewards, and sometimes tax-related purposes.
- **explanatoryNote**: Values are specified only for those merchant categories that are generally expected to originate retail financial transactions. Criteria for establishing a new category code includes (a) the merchant category is reasonable and substantially different from all other merchant categories currently represented in the list of code values; (b) the merchant category is separate and distinct from all other industries currently represented in the list of code values; (c) the proposal describes a merchant category or industry, and not a process; (d) the minimum annual sales volume of merchants included in the merchant category, taken as a whole, is USD 10 million; and (e) sufficient justification for the addition of a new code value is found.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
