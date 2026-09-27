---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: data protection requirement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Requirements defining how data about individuals is held. Example is the EU DA directive and laws, which make the
      data the property of the individual that data is about. Covers - what information i sheld - who information can be divulged
      to. - the individual's rights in respect of that information Privacy regulations cover most of this. EU defines "Personal
      Data" and "Sensitive Personal Data". For credit reference agencies the latter would be covered. More detail about whether
      they can divulge facts which are not subject to formal judgements etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/DataProtectionRequirement
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
title: data protection requirement
type: Ontology Class
---

# data protection requirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/DataProtectionRequirement>

## Definition

Requirements defining how data about individuals is held. Example is the EU DA directive and laws, which make the data the property of the individual that data is about. Covers - what information i sheld - who information can be divulged to. - the individual's rights in respect of that information Privacy regulations cover most of this. EU defines "Personal Data" and "Sensitive Personal Data". For credit reference agencies the latter would be covered. More detail about whether they can divulge facts which are not subject to formal judgements etc.

## Relationships

- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Annotations

- **label** (en): data protection requirement
- **definition** (en): Requirements defining how data about individuals is held. Example is the EU DA directive and laws, which make the data the property of the individual that data is about. Covers - what information i sheld - who information can be divulged to. - the individual's rights in respect of that information Privacy regulations cover most of this. EU defines "Personal Data" and "Sensitive Personal Data". For credit reference agencies the latter would be covered. More detail about whether they can divulge facts which are not subject to formal judgements etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
