---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redemption provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract provision enabling the issuer (writer) to regain possession through repayment of some stipulated price
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In general, redemption is synonymous with 'buy back' or 'cash in', depending on the kind of instrument. Redemption
      provisions are commonly applicable to the process of annulling a defeasible title, such as for a mortgage or tax sale,
      by paying the debt or fulfilling an obligation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: redemption provision
type: Ontology Class
---

# redemption provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision>

## Definition

contract provision enabling the issuer (writer) to regain possession through repayment of some stipulated price

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label**: redemption provision
- **definition**: contract provision enabling the issuer (writer) to regain possession through repayment of some stipulated price
- **explanatoryNote**: In general, redemption is synonymous with 'buy back' or 'cash in', depending on the kind of instrument. Redemption provisions are commonly applicable to the process of annulling a defeasible title, such as for a mortgage or tax sale, by paying the debt or fulfilling an obligation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
