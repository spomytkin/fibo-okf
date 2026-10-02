---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: ISO 4914:2021(en), Financial services - Unique product identifier (UPI)
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unique product identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters uniquely identifying an OTC derivative product that is reportable to a trade repository
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: "At a minimum, the UPI code is applicable to OTC derivative instruments falling under the following categories\
      \ of the Classification of Financial Instruments (ISO 10962):\n\t\t- Swaps (S)\n\t\t- Forwards (J)\n\t\t- Non-listed\
      \ and complex listed options (H)\n\t\t- Others (miscellaneous) (M)"
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: UPI
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "The UPI code consists of 12 alphanumeric characters decomposed as follows:\n\t\t- the two-character prefix 'QZ'\n\
      \t\t- nine alphanumeric characters (upper case A-Z and 0-9 only, excluding the vowel characters (A, E, I, O, U) and\
      \ the character Y) without separators or special characters\n\t\t- one alphanumeric check character (A-Z and 0-9 only,\
      \ excluding the vowel characters (A, E, I, O, U) and the character Y), calculated using the method specified in Annex\
      \ C of the specification document."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: unique product identifier
type: Ontology Class
---

# unique product identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier>

## Definition

sequence of characters uniquely identifying an OTC derivative product that is reportable to a trade repository

## Relationships

- **Subclass of**: [FinancialInstrumentIdentifier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- **Subclass of**: [StructuredIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: min qualified cardinality 0 of type [OverTheCounterDerivativeInstrument](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from of type [UniqueProductIdentifierServiceProvider](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider.md)

## Annotations

- **source**: ISO 4914:2021(en), Financial services - Unique product identifier (UPI)
- **label**: unique product identifier
- **definition**: sequence of characters uniquely identifying an OTC derivative product that is reportable to a trade repository
- **scopeNote**: At a minimum, the UPI code is applicable to OTC derivative instruments falling under the following categories of the Classification of Financial Instruments (ISO 10962): 		- Swaps (S) 		- Forwards (J) 		- Non-listed and complex listed options (H) 		- Others (miscellaneous) (M)
- **abbreviation**: UPI
- **explanatoryNote**: The UPI code consists of 12 alphanumeric characters decomposed as follows: 		- the two-character prefix 'QZ' 		- nine alphanumeric characters (upper case A-Z and 0-9 only, excluding the vowel characters (A, E, I, O, U) and the character Y) without separators or special characters 		- one alphanumeric check character (A-Z and 0-9 only, excluding the vowel characters (A, E, I, O, U) and the character Y), calculated using the method specified in Annex C of the specification document.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
