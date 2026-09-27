---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international bank account identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier for a bank account that is an expanded version of the basic bank account number (BBAN), intended for
      use internationally
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: For an account in Switzerland, suppose that an example domestic account number is 762 1162-3852.957. Suppose further
      that the bank identifier portion of that domestic account number is 762, or normalized for the BBAN is '00762'. For
      that example, the corresponding BBAN is '00762011623852957' and IBAN is 'CH9300762011623852957'.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IBAN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that international bank account numbers are formatted uniquely by country. A description of the country-specific
      formats is available from SWIFT (https://www.swift.com/), which is the ISO registrar for ISO 13616.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The IBAN structure is defined in ISO 13616-1 and consists of a two-letter ISO 3166-1 country code, followed by
      two check digits and up to thirty alphanumeric characters for a BBAN (Basic Bank Account Number) which has a fixed length
      per country and, included within it, a bank identifier with a fixed position and a fixed length per country. The check
      digits are calculated based on the scheme defined in ISO/IEC 7064 (MOD97-10).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: international bank account number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InternationalBankAccountIdentifier
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: international bank account identifier
type: Ontology Class
---

# international bank account identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InternationalBankAccountIdentifier>

## Definition

identifier for a bank account that is an expanded version of the basic bank account number (BBAN), intended for use internationally

## Relationships

- **Subclass of**: [BankAccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md)
- **Subclass of**: [StructuredIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [BasicBankAccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [GeographicRegionIdentifier](<https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier>)

## Annotations

- **label**: international bank account identifier
- **definition**: identifier for a bank account that is an expanded version of the basic bank account number (BBAN), intended for use internationally
- **example**: For an account in Switzerland, suppose that an example domestic account number is 762 1162-3852.957. Suppose further that the bank identifier portion of that domestic account number is 762, or normalized for the BBAN is '00762'. For that example, the corresponding BBAN is '00762011623852957' and IBAN is 'CH9300762011623852957'.
- **abbreviation**: IBAN
- **adaptedFrom**: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
- **explanatoryNote**: Note that international bank account numbers are formatted uniquely by country. A description of the country-specific formats is available from SWIFT (https://www.swift.com/), which is the ISO registrar for ISO 13616.
- **explanatoryNote**: The IBAN structure is defined in ISO 13616-1 and consists of a two-letter ISO 3166-1 country code, followed by two check digits and up to thirty alphanumeric characters for a BBAN (Basic Bank Account Number) which has a fixed length per country and, included within it, a bank identifier with a fixed position and a fixed length per country. The check digits are calculated based on the scheme defined in ISO/IEC 7064 (MOD97-10).
- **synonym**: international bank account number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
