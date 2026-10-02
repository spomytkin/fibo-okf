---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has option writer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the issuer of the option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically, the option writer collects the premium when the option is initially sold.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionIssuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionIssuer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasOptionWriter
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: has option writer
type: Ontology Property
---

# has option writer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasOptionWriter>

## Definition

indicates the issuer of the option

## Relationships

- **Domain**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)
- **Range**: [OptionIssuer](/concepts/fibo/DER/DerivativesContracts/Options/OptionIssuer.md)
- **Subproperty of**: [hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)

## Annotations

- **label**: has option writer
- **definition**: indicates the issuer of the option
- **explanatoryNote** (en): Typically, the option writer collects the premium when the option is initially sold.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
