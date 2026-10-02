---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan default proceeding
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: '[no definition] Further Review This is typically part of mortgagte servicing. THere would typically be a whole
      department dealing with this. Dealing with default, helping borrowers make payment Collections Default admin Foreclosure
      Reselling All dealt with by several sub departments. This requires subject matter experts in this area. 1. scoping Identify
      default as a possible state. This hands off to other business processes. Once you get into the default scenario we are
      talking about a proces that is going to fall into place over a period of time. The bank works out what to do with the
      default scenario, e.g. whether it restructures, forecloses, seeks restitution from the security (collateral). It does
      nto help us to understand the structure of the loan, rather tha consequences of the loan. If we were to further explore
      the default detail we would bring in other SMEs. And we would have to model a process flow. 1.1 impact on the pool of
      an MBS Loan Default Proceeding (special ase of legal thing) is an aspect of Default Management / Administratoin. there
      is also the State of the Loan. Sale / something / fulfilment / fiunduing / approved = servicing mode. Something happens
      (non payment) =&gt; Default Grace Period followed by negotiation. Some threshold whereby after a given amount of delinquency
      it needs to go into some other process moving towards foreclosure. Do State Diagram. Stages of loan.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanEvents/LegalProceeding.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LegalProceeding
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LoanDefaultProceeding
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: loan default proceeding
type: Ontology Class
---

# loan default proceeding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LoanDefaultProceeding>

## Definition

[no definition] Further Review This is typically part of mortgagte servicing. THere would typically be a whole department dealing with this. Dealing with default, helping borrowers make payment Collections Default admin Foreclosure Reselling All dealt with by several sub departments. This requires subject matter experts in this area. 1. scoping Identify default as a possible state. This hands off to other business processes. Once you get into the default scenario we are talking about a proces that is going to fall into place over a period of time. The bank works out what to do with the default scenario, e.g. whether it restructures, forecloses, seeks restitution from the security (collateral). It does nto help us to understand the structure of the loan, rather tha consequences of the loan. If we were to further explore the default detail we would bring in other SMEs. And we would have to model a process flow. 1.1 impact on the pool of an MBS Loan Default Proceeding (special ase of legal thing) is an aspect of Default Management / Administratoin. there is also the State of the Loan. Sale / something / fulfilment / fiunduing / approved = servicing mode. Something happens (non payment) =&gt; Default Grace Period followed by negotiation. Some threshold whereby after a given amount of delinquency it needs to go into some other process moving towards foreclosure. Do State Diagram. Stages of loan.

## Relationships

- **Subclass of**: [LegalProceeding](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/LegalProceeding.md)

## Annotations

- **label** (en): loan default proceeding
- **definition** (en): [no definition] Further Review This is typically part of mortgagte servicing. THere would typically be a whole department dealing with this. Dealing with default, helping borrowers make payment Collections Default admin Foreclosure Reselling All dealt with by several sub departments. This requires subject matter experts in this area. 1. scoping Identify default as a possible state. This hands off to other business processes. Once you get into the default scenario we are talking about a proces that is going to fall into place over a period of time. The bank works out what to do with the default scenario, e.g. whether it restructures, forecloses, seeks restitution from the security (collateral). It does nto help us to understand the structure of the loan, rather tha consequences of the loan. If we were to further explore the default detail we would bring in other SMEs. And we would have to model a process flow. 1.1 impact on the pool of an MBS Loan Default Proceeding (special ase of legal thing) is an aspect of Default Management / Administratoin. there is also the State of the Loan. Sale / something / fulfilment / fiunduing / approved = servicing mode. Something happens (non payment) =&gt; Default Grace Period followed by negotiation. Some threshold whereby after a given amount of delinquency it needs to go into some other process moving towards foreclosure. Do State Diagram. Stages of loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
