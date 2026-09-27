---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: https://www.actusfrf.org/taxonomy
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract type - call money
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cashflow classifier that applies to loans that are rolled over as long as they are not called
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Need to figure out whether this only applies to commercial loans and whether additional restrictions are needed
      to limit coverage to loans whose borrowers and lenders are financial institutions, possibly other things (short term?,
      interbank only?).
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Once called, they must be repaid after the stipulated notice period.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/hasCoverageDescription
    value: Interbank loans with call features.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: CLM
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-FixedIncome.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-FixedIncome
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-CallMoney
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS contract type - call money
type: Ontology Individual
---

# ACTUS contract type - call money

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-CallMoney>

## Definition

cashflow classifier that applies to loans that are rolled over as long as they are not called

## Relationships

- **Related to**: [AlgorithmicContractCategory-FixedIncome](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-FixedIncome.md)
- **Related to**: [AlgorithmicContractFamily-Basic](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **source**: https://www.actusfrf.org/taxonomy
- **label**: ACTUS contract type - call money
- **definition**: cashflow classifier that applies to loans that are rolled over as long as they are not called
- **editorialNote**: Need to figure out whether this only applies to commercial loans and whether additional restrictions are needed to limit coverage to loans whose borrowers and lenders are financial institutions, possibly other things (short term?, interbank only?).
- **note**: Once called, they must be repaid after the stipulated notice period.
- **hasCoverageDescription**: Interbank loans with call features.
- **hasTextValue**: CLM

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
