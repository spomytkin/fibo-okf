---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract type - convertible note
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cashflow classifier that applies to bonds with a call or put option
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Should this also only classify contracts that are convertible? Does this mean an additional restriction? Does it
      really apply to any sort of loan?
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: If the option is exercised, the underlying bond ceases to exist.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/hasCoverageDescription
    value: Callable and puttable bonds or loans.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: BNDCP
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-ConvertibleNote
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS contract type - convertible note
type: Ontology Individual
---

# ACTUS contract type - convertible note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-ConvertibleNote>

## Definition

cashflow classifier that applies to bonds with a call or put option

## Relationships

- **Related to**: [AlgorithmicContractCategory-Asymmetric](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric.md)
- **Related to**: [AlgorithmicContractFamily-Combined](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **label**: ACTUS contract type - convertible note
- **definition**: cashflow classifier that applies to bonds with a call or put option
- **editorialNote**: Should this also only classify contracts that are convertible? Does this mean an additional restriction? Does it really apply to any sort of loan?
- **note**: If the option is exercised, the underlying bond ceases to exist.
- **hasCoverageDescription**: Callable and puttable bonds or loans.
- **hasTextValue**: BNDCP

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
