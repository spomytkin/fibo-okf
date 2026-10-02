---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has governing jurisdiction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the jurisdiction governing the contract, as agreed by all parties
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'As modeled, this relationship combines two slightly different senses in which a Jurisdiction may be named in some
      Contract: the jurisdiction under whose laws the contract is deemed to be in force, and the jurisdiction under which
      the parties agree to submit in the event of any dispute resolution. ScopeNote: One thing to tease out is whether ''Dispute
      Resolution'' and other forms of ''Governing Law'' are one and the same thing or not. Dispute Resolution is uncontroversial,
      the question is whether there are other implications to Governing Law or if it''s the same thing. For instance I may
      undertake to behave as though I were responsible to a particular authority i.e., a particular set of statutes.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a written contract this is generally identified, for example, as Governing Law, namely the jurisdiction in which
      any disputes arising from the contract are to be resolved.
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasGoverningJurisdiction
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has governing jurisdiction
type: Ontology Property
---

# has governing jurisdiction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasGoverningJurisdiction>

## Definition

indicates the jurisdiction governing the contract, as agreed by all parties

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **Subproperty of**: [isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)

## Annotations

- **label**: has governing jurisdiction
- **definition**: indicates the jurisdiction governing the contract, as agreed by all parties
- **editorialNote**: As modeled, this relationship combines two slightly different senses in which a Jurisdiction may be named in some Contract: the jurisdiction under whose laws the contract is deemed to be in force, and the jurisdiction under which the parties agree to submit in the event of any dispute resolution. ScopeNote: One thing to tease out is whether 'Dispute Resolution' and other forms of 'Governing Law' are one and the same thing or not. Dispute Resolution is uncontroversial, the question is whether there are other implications to Governing Law or if it's the same thing. For instance I may undertake to behave as though I were responsible to a particular authority i.e., a particular set of statutes.
- **explanatoryNote**: In a written contract this is generally identified, for example, as Governing Law, namely the jurisdiction in which any disputes arising from the contract are to be resolved.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
