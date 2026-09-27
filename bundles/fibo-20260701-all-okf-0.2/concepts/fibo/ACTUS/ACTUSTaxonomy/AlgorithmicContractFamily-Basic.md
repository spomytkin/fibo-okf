---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: https://www.actusfrf.org/taxonomy
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: algorithmic contract family - basic
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract family classifier that applies to single (simple) contracts
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Basic, or atomic contracts include those individual contracts that have schedules associated with them, i.e., that
      have traditional maturity dates and future cash flows, or that represent demand deposits, i.e., accounts that have no
      structured maturity term, whose cash flows or amounts depend on counterparty behavior, as well as other assets such
      as stocks. Such contracts and related assets are typically bilateral.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: Basic
  different_from:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-CreditEnhancement.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-CreditEnhancement
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic
sources:
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: algorithmic contract family - basic
type: Ontology Individual
---

# algorithmic contract family - basic

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic>

## Definition

contract family classifier that applies to single (simple) contracts

## Relationships

- **Different from**: [AlgorithmicContractFamily-Combined](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md)
- **Different from**: [AlgorithmicContractFamily-CreditEnhancement](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-CreditEnhancement.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **source**: https://www.actusfrf.org/taxonomy
- **label**: algorithmic contract family - basic
- **definition**: contract family classifier that applies to single (simple) contracts
- **explanatoryNote**: Basic, or atomic contracts include those individual contracts that have schedules associated with them, i.e., that have traditional maturity dates and future cash flows, or that represent demand deposits, i.e., accounts that have no structured maturity term, whose cash flows or amounts depend on counterparty behavior, as well as other assets such as stocks. Such contracts and related assets are typically bilateral.
- **hasTextValue**: Basic

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
