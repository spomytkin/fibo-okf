---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: foreign exchange master agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: product-specific master agreement intended to reflect best market practice and to provide a standard agreement
      for participants in the foreign exchange markets
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Foreign Exchange Committee of the Federal Reserve Bank of New York has approved and authorized publication
      of the Foreign Exchange and Options Master Agreement to cover foreign exchange spot and forward transactions as well
      as currency options.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The International Foreign Exchange Master Agreement (IFEMA) was published jointly by the British Bankers' Association
      and The Foreign Exchange Committee of the Federal Reserve Bank of New York in 1993 (an amended version was published
      in 1995). Foreign exchange settlement netting provisions are specified in such master agreements.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: FX master agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/ForeignExchangeSettlementNettingProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.newyorkfed.org/medialibrary/microsites/fxc/files/guidefx.pdf
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/ForeignExchangeMasterAgreement
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: foreign exchange master agreement
type: Ontology Class
---

# foreign exchange master agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/ForeignExchangeMasterAgreement>

## Definition

product-specific master agreement intended to reflect best market practice and to provide a standard agreement for participants in the foreign exchange markets

## Relationships

- **See also**: [guidefx.pdf](<https://www.newyorkfed.org/medialibrary/microsites/fxc/files/guidefx.pdf>)
- **Subclass of**: [MasterAgreement](/concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [ForeignExchangeSettlementNettingProvision](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/ForeignExchangeSettlementNettingProvision.md)

## Annotations

- **label** (en): foreign exchange master agreement
- **definition** (en): product-specific master agreement intended to reflect best market practice and to provide a standard agreement for participants in the foreign exchange markets
- **explanatoryNote** (en): The Foreign Exchange Committee of the Federal Reserve Bank of New York has approved and authorized publication of the Foreign Exchange and Options Master Agreement to cover foreign exchange spot and forward transactions as well as currency options.
- **explanatoryNote** (en): The International Foreign Exchange Master Agreement (IFEMA) was published jointly by the British Bankers' Association and The Foreign Exchange Committee of the Federal Reserve Bank of New York in 1993 (an amended version was published in 1995). Foreign exchange settlement netting provisions are specified in such master agreements.
- **synonym**: FX master agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
