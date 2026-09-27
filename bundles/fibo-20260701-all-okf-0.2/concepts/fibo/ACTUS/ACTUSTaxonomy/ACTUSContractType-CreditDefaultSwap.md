---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract type - credit default swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cashflow classifier that applies to contracts for which a payment is triggered if one or more of the underlying
      counterparties defaults
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Is this really limited to CDS, or should it apply to anything (or maybe any derivative) where one of the parties
      to an underlying contract that triggers payment defaults?
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/hasCoverageDescription
    value: All sorts of credit default swaps.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: CDSWP
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
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-CreditDefaultSwap
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS contract type - credit default swap
type: Ontology Individual
---

# ACTUS contract type - credit default swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-CreditDefaultSwap>

## Definition

cashflow classifier that applies to contracts for which a payment is triggered if one or more of the underlying counterparties defaults

## Relationships

- **Related to**: [AlgorithmicContractCategory-Asymmetric](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric.md)
- **Related to**: [AlgorithmicContractFamily-Combined](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **label**: ACTUS contract type - credit default swap
- **definition**: cashflow classifier that applies to contracts for which a payment is triggered if one or more of the underlying counterparties defaults
- **editorialNote**: Is this really limited to CDS, or should it apply to anything (or maybe any derivative) where one of the parties to an underlying contract that triggers payment defaults?
- **hasCoverageDescription**: All sorts of credit default swaps.
- **hasTextValue**: CDSWP

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
