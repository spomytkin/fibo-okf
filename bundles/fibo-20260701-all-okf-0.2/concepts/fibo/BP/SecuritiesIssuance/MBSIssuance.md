---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: Ontology of the overall process of issuing mortgage backed securities. These are the process elements that are
      common to different kinds of MBS issuance (agency and private label).
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MBSIssuance
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2023 EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MBSIssuance.md
    predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Provisional
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/
sources:
- id: fibo-source-98ae1fbc1c
  resource: references/fibo/BP/SecuritiesIssuance/MBSIssuance.rdf
  sha256: 98ae1fbc1c6325c22ec32be6fe2c3b1c11bf20f64ae80d0087c27a7f332d20f1
  title: FIBO source BP/SecuritiesIssuance/MBSIssuance.rdf
title: MBSIssuance
type: Ontology Definition
---

# MBSIssuance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/>

## Relationships

- **Related to**: [DebtIssuance](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance.md)
- **Related to**: [IssuanceDocuments](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [MBSIssuance](/concepts/fibo/BP/SecuritiesIssuance/MBSIssuance.md)
- **Related to**: [Provisional](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md)

## Annotations

- **abstract**: Ontology of the overall process of issuing mortgage backed securities. These are the process elements that are common to different kinds of MBS issuance (agency and private label).
- **license**: https://opensource.org/licenses/MIT
- **label**: MBSIssuance
- **copyright**: Copyright (c) 2013-2023 EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
