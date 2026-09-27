---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts specific to marine finance, which involves financing vessel acquisitions for the
      spot market, time charters or bareboat charters, as well as the construction of work boats, and to finance the acquisition
      of vessels for scrapping.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Marine Finance Ontology
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2023 EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Provisional
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/
  - concept: /concepts/fibo/LOAN/LoansSpecific/MarineFinance.md
    predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/
sources:
- id: fibo-source-ab59d0379b
  resource: references/fibo/LOAN/LoansSpecific/MarineFinance.rdf
  sha256: ab59d0379b2ad3a710669ccbb048f639d29436b20df95d91770694bf7f22c84e
  title: FIBO source LOAN/LoansSpecific/MarineFinance.rdf
title: Marine Finance Ontology
type: Ontology Definition
---

# Marine Finance Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [Loans](/concepts/fibo/LOAN/LoansGeneral/Loans.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [MarineFinance](/concepts/fibo/LOAN/LoansSpecific/MarineFinance.md)
- **Related to**: [Provisional](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md)

## Annotations

- **abstract**: This ontology defines concepts specific to marine finance, which involves financing vessel acquisitions for the spot market, time charters or bareboat charters, as well as the construction of work boats, and to finance the acquisition of vessels for scrapping.
- **license**: https://opensource.org/licenses/MIT
- **label** (en): Marine Finance Ontology
- **copyright**: Copyright (c) 2015-2023 EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
