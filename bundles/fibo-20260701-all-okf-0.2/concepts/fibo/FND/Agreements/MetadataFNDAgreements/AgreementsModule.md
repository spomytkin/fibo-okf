---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This module includes ontologies describing agreements between parties and contracts that formalize those agreements.
      These cover written and verbal contracts, including contracts which may be transferred from one party to another. The
      latter form the basis for financial securities contracts. The Contracts ontology also describes fundamental properties
      of contracts such as contractual terms, contract parties and so on, many of which form the basis for more specialized
      financial industry concepts such as interest payment terms, bond issuers and so on.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://purl.org/dc/terms/title
    value: FIBO FND Agreements Module
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Foundations (FND) Agreements Module
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agreements module
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2023 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Module
  related_to:
  - concept: /concepts/fibo/FND/Agreements/Agreements.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://spec.edmcouncil.org/fibo/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/MetadataFNDAgreements/AgreementsModule
sources:
- id: fibo-source-b5883c4c67
  resource: references/fibo/FND/Agreements/MetadataFNDAgreements.rdf
  sha256: b5883c4c6704a8b48c411647113eeafc5d9a1e8e48abeb6d028ec8cdeda9e91a
  title: FIBO source FND/Agreements/MetadataFNDAgreements.rdf
title: agreements module
type: Ontology Individual
---

# agreements module

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/MetadataFNDAgreements/AgreementsModule>

## Relationships

- **Related to**: [Agreements](/concepts/fibo/FND/Agreements/Agreements.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **See also**: [fibo](<https://spec.edmcouncil.org/fibo/>)

## Annotations

- **abstract**: This module includes ontologies describing agreements between parties and contracts that formalize those agreements. These cover written and verbal contracts, including contracts which may be transferred from one party to another. The latter form the basis for financial securities contracts. The Contracts ontology also describes fundamental properties of contracts such as contractual terms, contract parties and so on, many of which form the basis for more specialized financial industry concepts such as interest payment terms, bond issuers and so on.
- **license**: https://opensource.org/licenses/MIT
- **title**: FIBO FND Agreements Module
- **title**: Financial Industry Business Ontology (FIBO) Foundations (FND) Agreements Module
- **label**: agreements module
- **copyright**: Copyright (c) 2017-2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2017-2023 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
